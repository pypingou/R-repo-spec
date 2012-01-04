%global packname  multinomRob
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.4
Release:          1%{?dist}
Summary:          Robust Estimation of Overdispersed Multinomial Regression Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.8-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rgenoud R-MASS R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-rgenoud R-MASS R-mvtnorm 

%description
MNL and overdispersed multinomial regression using robust (LQD and tanh)

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
%doc %{rlibdir}/multinomRob/DESCRIPTION
%doc %{rlibdir}/multinomRob/html
%{rlibdir}/multinomRob/libs
%{rlibdir}/multinomRob/Meta
%{rlibdir}/multinomRob/INDEX
%{rlibdir}/multinomRob/help
%{rlibdir}/multinomRob/R
%{rlibdir}/multinomRob/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.4-1
- initial package for Fedora