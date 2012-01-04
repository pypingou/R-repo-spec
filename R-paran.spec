%global packname  paran
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.3
Release:          1%{?dist}
Summary:          Horn's Test of Principal Components/Factors

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
paran is an implementation of Horn's technique for numerically and
graphically evaluating the components or factors retained in a principle
components analysis (PCA) or common factor analysis (FA). Horn's method
contrasts eigenvalues produced through a PCA or FA on a number of random
data sets of uncorrelated variables with the same number of variables and
observations as the experimental or observational data set to produce
eigenvalues for components or factors that are adjusted for the sample
error-induced inflation. Components with adjusted eigenvalues greater than
one are retained. paran may also be used to conduct parallel analysis
following Glorfeld's (1995) suggestions to reduce the likelihood of

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
%doc %{rlibdir}/paran/DESCRIPTION
%doc %{rlibdir}/paran/html
%{rlibdir}/paran/NAMESPACE
%{rlibdir}/paran/help
%{rlibdir}/paran/R
%{rlibdir}/paran/INDEX
%{rlibdir}/paran/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.3-1
- initial package for Fedora