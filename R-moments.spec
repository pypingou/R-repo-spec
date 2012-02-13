%global packname  moments
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.13
Release:          1%{dist}
Summary:          Moments, cumulants, skewness, kurtosis and related tests

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions to calculate: moments, Pearson's kurtosis, Geary's kurtosis and
skewness; tests related to them (Anscombe-Glynn, D'Agostino,

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
%doc %{rlibdir}/moments/html
%doc %{rlibdir}/moments/DESCRIPTION
%{rlibdir}/moments/R
%{rlibdir}/moments/NAMESPACE
%{rlibdir}/moments/help
%{rlibdir}/moments/INDEX
%{rlibdir}/moments/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.13-1
- Update to version 0.13

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.12-1
- initial package for Fedora