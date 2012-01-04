%global packname  EMT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Exact Multinomial Test: Goodness-of-Fit Test for Discrete Multivariate data

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package provides functions to carry out a Goodness-of-fit test for
discrete multivariate data. It is tested if a given observation is likely
to have occured under the assumption of an ab-initio model. A p-value can
be calculated using different distance measures between observed and
expected frequencies. A Monte Carlo method is provided to make the package
capable of solving high-dimensional problems.

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
%doc %{rlibdir}/EMT/DESCRIPTION
%doc %{rlibdir}/EMT/html
%{rlibdir}/EMT/R
%{rlibdir}/EMT/NAMESPACE
%{rlibdir}/EMT/help
%{rlibdir}/EMT/INDEX
%{rlibdir}/EMT/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora