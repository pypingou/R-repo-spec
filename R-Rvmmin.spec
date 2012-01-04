%global packname  Rvmmin
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2011.5.091
Release:          1%{?dist}
Summary:          Variable metric nonlinear function minimization with bounds constraints

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011-5.091.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-numDeriv 

BuildRequires:    R-devel tex(latex) R-numDeriv 

%description
Variable metric nonlinear function minimization with bounds constraints

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
%doc %{rlibdir}/Rvmmin/html
%doc %{rlibdir}/Rvmmin/DESCRIPTION
%{rlibdir}/Rvmmin/NAMESPACE
%{rlibdir}/Rvmmin/help
%{rlibdir}/Rvmmin/R
%{rlibdir}/Rvmmin/INDEX
%{rlibdir}/Rvmmin/demo
%{rlibdir}/Rvmmin/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.5.091-1
- initial package for Fedora