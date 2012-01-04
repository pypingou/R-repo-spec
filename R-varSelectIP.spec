%global packname  varSelectIP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Objective Bayes Model Selection

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-MASS R-mvtnorm 

%description
Objective Bayes Variable Selection in Linear Regression and Probit models.

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
%doc %{rlibdir}/varSelectIP/html
%doc %{rlibdir}/varSelectIP/NEWS
%doc %{rlibdir}/varSelectIP/DESCRIPTION
%{rlibdir}/varSelectIP/NAMESPACE
%{rlibdir}/varSelectIP/Meta
%{rlibdir}/varSelectIP/INDEX
%{rlibdir}/varSelectIP/help
%{rlibdir}/varSelectIP/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora