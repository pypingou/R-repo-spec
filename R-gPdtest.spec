%global packname  gPdtest
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Bootstrap goodness-of-fit test for the generalized Pareto distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package computes the bootstrap goodness-of-fit test for the
generalized Pareto distribution by Villasenor-Alva and Gonzalez-Estrada
(2009). The null hypothesis includes heavy and non-heavy tailed gPd's. A
function for fitting the gPd to data using the parameter estimation
methods proposed in the same article is also provided.

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
%doc %{rlibdir}/gPdtest/DESCRIPTION
%doc %{rlibdir}/gPdtest/html
%{rlibdir}/gPdtest/help
%{rlibdir}/gPdtest/Meta
%{rlibdir}/gPdtest/R
%{rlibdir}/gPdtest/INDEX
%{rlibdir}/gPdtest/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4-1
- initial package for Fedora