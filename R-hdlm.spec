%global packname  hdlm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Fitting High Dimensional Linear Models

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lars R-boot R-plus 
Requires:         R-quantreg 

BuildRequires:    R-devel tex(latex) R-lars R-boot R-plus
BuildRequires:    R-quantreg 


%description
Mimics the lm function found in the recommended package stats to fit high
dimensional regression models with point estimates, standard errors, and
p-values. Methods for printing and summarizing the results are given.
Supports lasso estimator, Dantzig selector, mc+, root-lasso, and scad.
Methods are provided for the resulting class hdlm corresponding to methods
for the class lm.

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
%doc %{rlibdir}/hdlm/html
%doc %{rlibdir}/hdlm/DESCRIPTION
%{rlibdir}/hdlm/INDEX
%{rlibdir}/hdlm/Meta
%{rlibdir}/hdlm/R
%{rlibdir}/hdlm/NAMESPACE
%{rlibdir}/hdlm/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora