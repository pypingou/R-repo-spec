%global packname  sde
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.10
Release:          1%{?dist}
Summary:          Simulation and Inference for Stochastic Differential Equations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-stats4 R-fda R-zoo 

BuildRequires:    R-devel tex(latex) R-MASS R-stats4 R-fda R-zoo 

%description
Companion package to the book Simulation and Inference for Stochastic
Differential Equations With R Examples, ISBN 978-0-387-75838-1, Springer,

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
%doc %{rlibdir}/sde/DESCRIPTION
%doc %{rlibdir}/sde/doc
%doc %{rlibdir}/sde/html
%{rlibdir}/sde/book
%{rlibdir}/sde/libs
%{rlibdir}/sde/Meta
%{rlibdir}/sde/R
%{rlibdir}/sde/NAMESPACE
%{rlibdir}/sde/data
%{rlibdir}/sde/help
%{rlibdir}/sde/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.10-1
- initial package for Fedora