%global packname  ebal
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Entropy reweighting to create balanced samples

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Package implements entropy balancing, a data preprocessing procedure that
allows users to reweight a dataset such that the covariate distributions
in the reweighted data satisfy a set of user specified moment conditions.
This can be useful to create balanced samples in observational studies
with a binary treatment where the control group data can be reweighted to
match the covariate moments in the treatment group. Entropy balancing can
also be used to reweight a survey sample to known characteristics from a
target population. This package is currently in alpha phase (feedback is

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
%doc %{rlibdir}/ebal/DESCRIPTION
%doc %{rlibdir}/ebal/html
%{rlibdir}/ebal/help
%{rlibdir}/ebal/Meta
%{rlibdir}/ebal/R
%{rlibdir}/ebal/INDEX
%{rlibdir}/ebal/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora