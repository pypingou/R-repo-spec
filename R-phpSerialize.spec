%global packname  phpSerialize
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.01
Release:          1%{?dist}
Summary:          Serialize R to PHP associative array

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-01.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Serializes R objects for import by PHP into an associative array. Can be
used to build interactive web pages with R.

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
%doc %{rlibdir}/phpSerialize/DESCRIPTION
%doc %{rlibdir}/phpSerialize/html
%{rlibdir}/phpSerialize/web
%{rlibdir}/phpSerialize/Meta
%{rlibdir}/phpSerialize/R
%{rlibdir}/phpSerialize/NAMESPACE
%{rlibdir}/phpSerialize/help
%{rlibdir}/phpSerialize/sample
%{rlibdir}/phpSerialize/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.01-1
- initial package for Fedora