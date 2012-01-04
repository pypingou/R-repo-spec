%global packname  lss
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.52
Release:          1%{?dist}
Summary:          the accelerated failure time model to right censored data based on least-squares principle

Group:            Applications/Engineering 
License:          GPL version 2 or later
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-quantreg 


BuildRequires:    R-devel tex(latex) R-quantreg



%description
Due to lack of proper inference procedure and software, the ordinary
linear regression model is seldom used in practice for the analysis of
right censored data. This paper presents an S-Plus/R program that
implements a recently developed inference procedure (Jin, Lin and Ying,
2006)\cite{Jin} for the accelerated failure time model based on the
least-squares principle.

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
%doc %{rlibdir}/lss/DESCRIPTION
%doc %{rlibdir}/lss/html
%{rlibdir}/lss/R
%{rlibdir}/lss/data
%{rlibdir}/lss/NAMESPACE
%{rlibdir}/lss/INDEX
%{rlibdir}/lss/Meta
%{rlibdir}/lss/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.52-1
- initial package for Fedora