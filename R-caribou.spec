%global packname  caribou
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Estimation of caribou abundance

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package implements the methodology found in the article by Rivest,
L.-P., Couturier, S. and Crepeau, H. (1998) about caribou abundance
estimation. It also includes a function based on the Lincoln-Petersen
Index as applied to radio-telemetry data by White and Garrott (1990).

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
%doc %{rlibdir}/caribou/DESCRIPTION
%doc %{rlibdir}/caribou/html
%{rlibdir}/caribou/Meta
%{rlibdir}/caribou/INDEX
%{rlibdir}/caribou/NAMESPACE
%{rlibdir}/caribou/help
%{rlibdir}/caribou/data
%{rlibdir}/caribou/R

%changelog
* Mon Dec 05 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora