%global packname  CommonTrend
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.1
Release:          1%{?dist}
Summary:          Extract and plot common trends from a cointegration system. Calculate P-value for Johansen Statistics.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-methods R-MASS R-urca 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-methods R-MASS R-urca 


%description
Directly extract and plot common trends from cointegration systems using
different approaches, currenctly including Kasa (1992) and Gonzalo and
Granger (1995). The approach proposed by Gonzalo and Granger, also known
as Permanent-Transitory Decomposition, is widely used in Macroeconomics
and Market Microstructure literature. The Kasa's approach has a nice
property that it only uses the super consistent estimater: the
cointegration vector 'beta'. In addition, this package can also calculate
P-value for Johansen Statistics according to the approximation method
proposed by Doornik(1998).

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
%doc %{rlibdir}/CommonTrend/DESCRIPTION
%doc %{rlibdir}/CommonTrend/html
%{rlibdir}/CommonTrend/R
%{rlibdir}/CommonTrend/data
%{rlibdir}/CommonTrend/INDEX
%{rlibdir}/CommonTrend/help
%{rlibdir}/CommonTrend/NAMESPACE
%{rlibdir}/CommonTrend/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.1-1
- initial package for Fedora