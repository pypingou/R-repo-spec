%global packname  Survgini
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          The Gini concentration test for survival data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
The Gini concentration test for survival data is a nonparametric test
based on the Gini index for testing the equality of two survival
distributions from the point of view of concentration. The package
compares different nonparametric tests (asymptotic Gini test, permutation
Gini test, log-rank test, Gray-Tsiatis test and Wilcoxon test) and
computes their p-values.

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
%doc %{rlibdir}/Survgini/html
%doc %{rlibdir}/Survgini/DESCRIPTION
%{rlibdir}/Survgini/INDEX
%{rlibdir}/Survgini/Meta
%{rlibdir}/Survgini/R
%{rlibdir}/Survgini/NAMESPACE
%{rlibdir}/Survgini/help

%changelog
* Sat Dec 03 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora