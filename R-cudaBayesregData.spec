%global packname  cudaBayesregData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.10
Release:          1%{?dist}
Summary:          Data sets for the examples used in the package "cudaBayesreg"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
FMRI data sets used in the examples of "cudaBayesreg". Data sets have been
separated from the main package "cudaBayesreg" for convenience.

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
%doc %{rlibdir}/cudaBayesregData/DESCRIPTION
%doc %{rlibdir}/cudaBayesregData/html
%{rlibdir}/cudaBayesregData/extdata
%{rlibdir}/cudaBayesregData/INDEX
%{rlibdir}/cudaBayesregData/Meta
%{rlibdir}/cudaBayesregData/NAMESPACE
%{rlibdir}/cudaBayesregData/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.10-1
- initial package for Fedora