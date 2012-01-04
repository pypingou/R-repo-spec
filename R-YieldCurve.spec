%global packname  YieldCurve
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.1
Release:          1%{?dist}
Summary:          Modelling and estimation of the yield curve

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Modelling the yield curve with some parametric models. The models
implemented are: Nelson-Siegel, Diebold-Li and Svensson. The package also
includes the data of the term structure of interest rate of Federal
Reserve Bank and European Central Bank.

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
%doc %{rlibdir}/YieldCurve/html
%doc %{rlibdir}/YieldCurve/DESCRIPTION
%doc %{rlibdir}/YieldCurve/CITATION
%{rlibdir}/YieldCurve/NAMESPACE
%{rlibdir}/YieldCurve/R
%{rlibdir}/YieldCurve/Meta
%{rlibdir}/YieldCurve/data
%{rlibdir}/YieldCurve/help
%{rlibdir}/YieldCurve/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1-1
- initial package for Fedora