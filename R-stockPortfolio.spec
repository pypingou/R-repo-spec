%global packname  stockPortfolio
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Build stock models and analyze stock portfolios.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Download stock data, build single index, constant correlation, and
multigroup models, and estimate optimal stock portfolios. Plotting
functions for the portfolio possibilities curve and portfolio cloud are
included. A function to test a portfolio on a data set is also provided.

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
%doc %{rlibdir}/stockPortfolio/DESCRIPTION
%doc %{rlibdir}/stockPortfolio/html
%{rlibdir}/stockPortfolio/data
%{rlibdir}/stockPortfolio/NAMESPACE
%{rlibdir}/stockPortfolio/R
%{rlibdir}/stockPortfolio/INDEX
%{rlibdir}/stockPortfolio/help
%{rlibdir}/stockPortfolio/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora