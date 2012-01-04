%global packname  PresenceAbsence
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Presence-Absence Model Evaluation.

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides a set of functions useful when evaluating the
results of presence-absence models. Package includes functions for
calculating threshold dependant measures such as confusion matrices, pcc,
sensitivity, specificity, and Kappa, and produces plots of each measure as
the threshold is varied. It will calculate optimal threshold choice
according to a choice of optimization criteria. It also includes functions
to plot the threshold independent ROC curves along with the associated AUC
(area under the curve).

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
%doc %{rlibdir}/PresenceAbsence/html
%doc %{rlibdir}/PresenceAbsence/CITATION
%doc %{rlibdir}/PresenceAbsence/DESCRIPTION
%{rlibdir}/PresenceAbsence/R
%{rlibdir}/PresenceAbsence/Meta
%{rlibdir}/PresenceAbsence/data
%{rlibdir}/PresenceAbsence/INDEX
%{rlibdir}/PresenceAbsence/demo
%{rlibdir}/PresenceAbsence/help
%{rlibdir}/PresenceAbsence/CHANGELOG
%{rlibdir}/PresenceAbsence/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.5-1
- initial package for Fedora