%global packname  SNPRelate
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{dist}
Summary:          Parallel Computing Toolset for genome-wide association studies

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gdsfmt 


BuildRequires:    R-devel tex(latex) R-gdsfmt



%description
A high-performance computing package for relatedness, linkage
disequilibrium and principal component analysis in GWAS.

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
%doc %{rlibdir}/SNPRelate/html
%doc %{rlibdir}/SNPRelate/DESCRIPTION
%{rlibdir}/SNPRelate/help
%{rlibdir}/SNPRelate/INDEX
%{rlibdir}/SNPRelate/data
%{rlibdir}/SNPRelate/NAMESPACE
%{rlibdir}/SNPRelate/extdata
%{rlibdir}/SNPRelate/R
%{rlibdir}/SNPRelate/libs
%{rlibdir}/SNPRelate/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.2-1
- Update to version 0.9.2

* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.1-1
- initial package for Fedora