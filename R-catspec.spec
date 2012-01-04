%global packname  catspec
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.95
Release:          1%{?dist}
Summary:          Special models for categorical variables

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
`sqtab' contains a set of functions for estimating loglinear models for
square tables such as quasi-independence, symmetry, uniform association.
`mclgen' restructures a dataframe to enable the estimation of a
multinomial logistic model using the conditional logit program `clogit'.
This allows greater flexibility in imposing constraints on the response
variable. One application is to specify aforementioned models for square
tables as multinomial logistic models with covariates at the respondent
level. `ctab' simplifies the production of (multiway( percentage tables.

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
%doc %{rlibdir}/catspec/html
%doc %{rlibdir}/catspec/DESCRIPTION
%{rlibdir}/catspec/NAMESPACE
%{rlibdir}/catspec/INDEX
%{rlibdir}/catspec/help
%{rlibdir}/catspec/data
%{rlibdir}/catspec/Meta
%{rlibdir}/catspec/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.95-1
- initial package for Fedora