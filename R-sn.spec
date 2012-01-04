%global packname  sn
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.17
Release:          1%{?dist}
Summary:          The skew-normal and skew-t distributions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-17.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mnormt 

BuildRequires:    R-devel tex(latex) R-mnormt 

%description
Functions for manipulating skew-normal and skew-t probability
distributions, and for fitting them to data, in the scalar and in the
multivariate case.

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
%doc %{rlibdir}/sn/COPYING
%doc %{rlibdir}/sn/CITATION
%doc %{rlibdir}/sn/DESCRIPTION
%doc %{rlibdir}/sn/html
%{rlibdir}/sn/R
%{rlibdir}/sn/help
%{rlibdir}/sn/NAMESPACE
%{rlibdir}/sn/Meta
%{rlibdir}/sn/INDEX
%{rlibdir}/sn/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.17-1
- initial package for Fedora