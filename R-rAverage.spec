%global packname  rAverage
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Parameter estimation for the Averaging model of Information Integration Theory

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-tcltk R-foreign 

BuildRequires:    R-devel tex(latex) R-methods R-tcltk R-foreign 

%description
Parameter estimation for the Averaging model of Anderson's Information
Integration Theory

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
%doc %{rlibdir}/rAverage/html
%doc %{rlibdir}/rAverage/DESCRIPTION
%{rlibdir}/rAverage/Meta
%{rlibdir}/rAverage/data
%{rlibdir}/rAverage/libs
%{rlibdir}/rAverage/R
%{rlibdir}/rAverage/INDEX
%{rlibdir}/rAverage/NAMESPACE
%{rlibdir}/rAverage/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.5-1
- initial package for Fedora