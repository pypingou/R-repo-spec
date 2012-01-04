%global packname  mixedQF
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Estimator with Qudratics Forms in Mixeds Models

Group:            Applications/Engineering 
License:          FreeBSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nnet R-MASS 

BuildRequires:    R-devel tex(latex) R-nnet R-MASS 

%description
Compute Estimator of variance with quadratic forms, and computes test on a
linar contrasts in fixed effects

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
%doc %{rlibdir}/mixedQF/html
%doc %{rlibdir}/mixedQF/DESCRIPTION
%{rlibdir}/mixedQF/Meta
%{rlibdir}/mixedQF/help
%{rlibdir}/mixedQF/data
%{rlibdir}/mixedQF/NAMESPACE
%{rlibdir}/mixedQF/INDEX
%{rlibdir}/mixedQF/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora