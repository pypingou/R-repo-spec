%global packname  tlemix
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.9
Release:          1%{?dist}
Summary:          Trimmed Maximum Likelihood Estimation

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-flexmix 
Requires:         R-methods R-flexmix R-modeltools R-stats4 

BuildRequires:    R-devel tex(latex) R-flexmix
BuildRequires:    R-methods R-flexmix R-modeltools R-stats4 


%description
TLE implements a general framework for robust fitting of finite mixture
models. Parameter estimation is performed using the EM algorithm.

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
%doc %{rlibdir}/tlemix/DESCRIPTION
%doc %{rlibdir}/tlemix/html
%{rlibdir}/tlemix/R
%{rlibdir}/tlemix/Meta
%{rlibdir}/tlemix/data
%{rlibdir}/tlemix/INDEX
%{rlibdir}/tlemix/help
%{rlibdir}/tlemix/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.9-1
- initial package for Fedora