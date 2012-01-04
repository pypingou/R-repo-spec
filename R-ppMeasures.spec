%global packname  ppMeasures
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Point pattern distances and prototypes.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package focuses on distances and prototypes for point patterns. There
are three algorithms provided to compute spike-time distance, and one of
these algorithms is generalized to compute variations of spike-time
distance. Multiple algorithms are also provided to estimate prototypes of
collections of point patterns.

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
%doc %{rlibdir}/ppMeasures/html
%doc %{rlibdir}/ppMeasures/DESCRIPTION
%{rlibdir}/ppMeasures/INDEX
%{rlibdir}/ppMeasures/data
%{rlibdir}/ppMeasures/help
%{rlibdir}/ppMeasures/Meta
%{rlibdir}/ppMeasures/R
%{rlibdir}/ppMeasures/libs
%{rlibdir}/ppMeasures/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora