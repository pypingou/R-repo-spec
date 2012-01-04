%global packname  rvgtest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Tools for Analyzing Non-Uniform Pseudo-Random Variate Generators

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Test suite for non-uniform pseudo-random number generators.

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
%doc %{rlibdir}/rvgtest/DESCRIPTION
%doc %{rlibdir}/rvgtest/doc
%doc %{rlibdir}/rvgtest/html
%doc %{rlibdir}/rvgtest/NEWS
%{rlibdir}/rvgtest/help
%{rlibdir}/rvgtest/NAMESPACE
%{rlibdir}/rvgtest/Meta
%{rlibdir}/rvgtest/R
%{rlibdir}/rvgtest/libs
%{rlibdir}/rvgtest/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.0-1
- initial package for Fedora