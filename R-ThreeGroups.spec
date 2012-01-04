%global packname  ThreeGroups
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          ML Estimator for Baseline-Placebo-Treatment (Three-group) designs

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package implements the Maximum Likelihood estimator for three-group
designs proposed by Gerber, Green, Kaplan, and Kern (2010).

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
%doc %{rlibdir}/ThreeGroups/html
%doc %{rlibdir}/ThreeGroups/DESCRIPTION
%{rlibdir}/ThreeGroups/NAMESPACE
%{rlibdir}/ThreeGroups/Meta
%{rlibdir}/ThreeGroups/help
%{rlibdir}/ThreeGroups/INDEX
%{rlibdir}/ThreeGroups/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora