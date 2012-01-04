%global packname  tweeDEseq
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          RNA-seq data analysis using the Poisson-Tweedie family of distributions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-MASS R-limma R-edgeR 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-MASS R-limma R-edgeR 


%description
Differential expression analysis of RNA-seq using the Poisson-Tweedie
family of distributions.

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
%doc %{rlibdir}/tweeDEseq/html
%doc %{rlibdir}/tweeDEseq/DESCRIPTION
%doc %{rlibdir}/tweeDEseq/doc
%{rlibdir}/tweeDEseq/NAMESPACE
%{rlibdir}/tweeDEseq/INDEX
%{rlibdir}/tweeDEseq/help
%{rlibdir}/tweeDEseq/Meta
%{rlibdir}/tweeDEseq/data
%{rlibdir}/tweeDEseq/R
%{rlibdir}/tweeDEseq/libs

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora