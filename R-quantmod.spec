%global packname  quantmod
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.17
Release:          1%{?dist}
Summary:          Quantitative Financial Modelling Framework

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-17.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Defaults R-xts R-zoo R-TTR R-methods 


BuildRequires:    R-devel tex(latex) R-Defaults R-xts R-zoo R-TTR R-methods



%description
Specify, build, trade, and analyse quantitative financial trading

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.17-1
- initial package for Fedora