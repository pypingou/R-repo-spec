%global packname  IlluminaHumanMethylation450k.db
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.6
Release:          1%{?dist}
Summary:          Illumina Human Methylation 450k annotation data

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-AnnotationDbi R-org.Hs.eg.db 
Requires:         R-methods R-AnnotationDbi 

BuildRequires:    R-devel tex(latex) R-methods R-AnnotationDbi R-org.Hs.eg.db
BuildRequires:    R-methods R-AnnotationDbi 


%description
Illumina Human Methylation 450k annotation data (chip
IlluminaHumanMethylation450k) assembled using data from public

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
%changelog
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.6-1
- initial package for Fedora