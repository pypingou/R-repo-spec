%global packname  mixreg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          Functions to fit mixtures of regressions.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Fits mixtures of (possibly multivariate) regressions (which has been
described as doing ANCOVA when you don't know the levels).

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
%doc %{rlibdir}/mixreg/html
%doc %{rlibdir}/mixreg/DESCRIPTION
%{rlibdir}/mixreg/Meta
%{rlibdir}/mixreg/NAMESPACE
%{rlibdir}/mixreg/aphids.dat
%{rlibdir}/mixreg/aphids.R
%{rlibdir}/mixreg/R
%{rlibdir}/mixreg/help
%{rlibdir}/mixreg/READ_ME
%{rlibdir}/mixreg/INDEX
%{rlibdir}/mixreg/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.4-1
- initial package for Fedora