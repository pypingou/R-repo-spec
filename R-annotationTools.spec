%global packname  annotationTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Annotate microarrays and perform cross-species gene expression analyses using flat file databases.

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-stats 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-stats 


%description
Functions to annotate microarrays, find orthologs, and integrate
heterogeneous gene expression profiles using annotation and other
molecular biology information available as flat file database (plain text

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/annotationTools/html
%doc %{rlibdir}/annotationTools/DESCRIPTION
%doc %{rlibdir}/annotationTools/CITATION
%doc %{rlibdir}/annotationTools/doc
%{rlibdir}/annotationTools/R
%{rlibdir}/annotationTools/data
%{rlibdir}/annotationTools/NAMESPACE
%{rlibdir}/annotationTools/Meta
%{rlibdir}/annotationTools/help
%{rlibdir}/annotationTools/extdata
%{rlibdir}/annotationTools/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora