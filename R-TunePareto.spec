%global packname  TunePareto
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Multi-objective parameter tuning for classifiers

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Generic methods for parameter tuning of classification algorithms using
multiple scoring functions

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
%doc %{rlibdir}/TunePareto/DESCRIPTION
%doc %{rlibdir}/TunePareto/html
%{rlibdir}/TunePareto/Meta
%{rlibdir}/TunePareto/libs
%{rlibdir}/TunePareto/R
%{rlibdir}/TunePareto/INDEX
%{rlibdir}/TunePareto/NAMESPACE
%{rlibdir}/TunePareto/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora