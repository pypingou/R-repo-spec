%global packname  GenSA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.99.3
Release:          1%{?dist}
Summary:          R functions for Generalized Simulated Annealing

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package searches for global minimum of a very complex non-linear
objective function with a very large number of optima.

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
%doc %{rlibdir}/GenSA/DESCRIPTION
%doc %{rlibdir}/GenSA/html
%doc %{rlibdir}/GenSA/NEWS
%doc %{rlibdir}/GenSA/CITATION
%{rlibdir}/GenSA/R
%{rlibdir}/GenSA/help
%{rlibdir}/GenSA/libs
%{rlibdir}/GenSA/LICENSE
%{rlibdir}/GenSA/NAMESPACE
%{rlibdir}/GenSA/INDEX
%{rlibdir}/GenSA/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.3-1
- initial package for Fedora