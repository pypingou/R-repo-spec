%global packname  ChemometricsWithRData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Data for package ChemometricsWithR

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package provides data sets used in the book "Chemometrics with R -
Multivariate Data Analysis in the Natural Sciences and Life Sciences" by
Ron Wehrens, Springer (2011).

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
%doc %{rlibdir}/ChemometricsWithRData/html
%doc %{rlibdir}/ChemometricsWithRData/DESCRIPTION
%{rlibdir}/ChemometricsWithRData/help
%{rlibdir}/ChemometricsWithRData/data
%{rlibdir}/ChemometricsWithRData/NAMESPACE
%{rlibdir}/ChemometricsWithRData/INDEX
%{rlibdir}/ChemometricsWithRData/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora