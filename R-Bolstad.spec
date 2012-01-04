%global packname  Bolstad
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.20
Release:          1%{?dist}
Summary:          Bolstad functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-20.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A set of R functions and data sets for the book Introduction to Bayesian
Statistics, Bolstad, W.M. (2007), John Wiley & Sons ISBN 0-471-27020-2

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
%doc %{rlibdir}/Bolstad/DESCRIPTION
%doc %{rlibdir}/Bolstad/html
%{rlibdir}/Bolstad/NAMESPACE
%{rlibdir}/Bolstad/INDEX
%{rlibdir}/Bolstad/help
%{rlibdir}/Bolstad/data
%{rlibdir}/Bolstad/Meta
%{rlibdir}/Bolstad/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.20-1
- initial package for Fedora