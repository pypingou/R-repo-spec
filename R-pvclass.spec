%global packname  pvclass
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          P-values for Classification

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
Computes nonparametric p-values for the potential class memberships of new
observations as well as cross-validated p-values for the training data.
The p-values are based on permutation tests applied to an estimated
Bayesian likelihood ratio, using a plug-in statistic for the Gaussian
model, 'k nearest neighbors' or 'weighted nearest neighbors'.
Additionally, it provides graphical displays and quantitative analyses of
the p-values.

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
%doc %{rlibdir}/pvclass/DESCRIPTION
%doc %{rlibdir}/pvclass/html
%{rlibdir}/pvclass/data
%{rlibdir}/pvclass/INDEX
%{rlibdir}/pvclass/Meta
%{rlibdir}/pvclass/help
%{rlibdir}/pvclass/NAMESPACE
%{rlibdir}/pvclass/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora