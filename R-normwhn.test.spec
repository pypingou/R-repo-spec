%global packname  normwhn.test
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Normality and White Noise Testing

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Includes Omnibus Univariate and Multivariate Normality Tests (See Doornik
and Hansen (1994)). One variation allows for the possibility of weak
dependence rather than independence in the variable(s). Also included is
an univariate white noise test where the null hypothesis is "white noise"
rather than strict "white noise".

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
%doc %{rlibdir}/normwhn.test/html
%doc %{rlibdir}/normwhn.test/DESCRIPTION
%{rlibdir}/normwhn.test/INDEX
%{rlibdir}/normwhn.test/R
%{rlibdir}/normwhn.test/NAMESPACE
%{rlibdir}/normwhn.test/help
%{rlibdir}/normwhn.test/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora