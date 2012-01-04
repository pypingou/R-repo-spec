%global packname  REGENT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          REGENT: Risk Estimation for Genetic and Environmental Traits

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Produces population distribution of disease risk and statistical risk
categories, and predicts risks for individuals with genotype information

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
%doc %{rlibdir}/REGENT/DESCRIPTION
%doc %{rlibdir}/REGENT/html
%{rlibdir}/REGENT/NAMESPACE
%{rlibdir}/REGENT/data
%{rlibdir}/REGENT/Meta
%{rlibdir}/REGENT/R
%{rlibdir}/REGENT/INDEX
%{rlibdir}/REGENT/help

%changelog
* Sun Dec 04 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora