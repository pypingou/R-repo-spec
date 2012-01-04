%global packname  GWASExactHW
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Exact Hardy-Weinburg testing for Genome Wide Association Studies

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains a function to do exact Hardy-Weinburg testing (using
Fisher's test) for SNP genotypes as typically obtained in a Genome Wide
Association Study (GWAS).

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
%doc %{rlibdir}/GWASExactHW/DESCRIPTION
%doc %{rlibdir}/GWASExactHW/html
%{rlibdir}/GWASExactHW/NAMESPACE
%{rlibdir}/GWASExactHW/libs
%{rlibdir}/GWASExactHW/help
%{rlibdir}/GWASExactHW/R
%{rlibdir}/GWASExactHW/Meta
%{rlibdir}/GWASExactHW/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora