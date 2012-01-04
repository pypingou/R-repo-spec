%global packname  ACCLMA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          ACC & LMA Graph Plotting

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The main function is plotLMA(sourcefile,header) that takes a data set and
plots the appropriate LMA and ACC graphs. If no sourcefile (a string) was
passed, a manual data entry window is opened. The header parameter
indicates by TRUE/FALSE (false by default) if the source CSV file has a
head row or not. The data set should contain only one independent variable
(X) and one dependent varialbe (Y) and can contain a weight for each

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
%doc %{rlibdir}/ACCLMA/html
%doc %{rlibdir}/ACCLMA/DESCRIPTION
%{rlibdir}/ACCLMA/INDEX
%{rlibdir}/ACCLMA/Meta
%{rlibdir}/ACCLMA/NAMESPACE
%{rlibdir}/ACCLMA/help
%{rlibdir}/ACCLMA/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora