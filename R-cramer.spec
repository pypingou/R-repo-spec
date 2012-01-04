%global packname  cramer
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Multivariate nonparametric Cramer-Test for the two-sample-problem

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-boot 

BuildRequires:    R-devel tex(latex) R-boot 

%description
Provides R routine for the so called two-sample Cramer-Test. This not
distribution free, nonparametric two-sample-test can be applied on
multivariate data as well as univariate data. It offers two possiblities
to approximate the critical value both of which are included in this

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
%doc %{rlibdir}/cramer/html
%doc %{rlibdir}/cramer/DESCRIPTION
%{rlibdir}/cramer/R
%{rlibdir}/cramer/Meta
%{rlibdir}/cramer/help
%{rlibdir}/cramer/INDEX
%{rlibdir}/cramer/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- initial package for Fedora