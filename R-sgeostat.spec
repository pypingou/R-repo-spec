%global packname  sgeostat
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.23
Release:          1%{?dist}
Summary:          An Object-oriented Framework for Geostatistical Modeling in S+

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-23.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-grDevices R-graphics 

BuildRequires:    R-devel tex(latex) R-stats R-grDevices R-graphics 

%description
An Object-oriented Framework for Geostatistical Modeling in S+

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
%doc %{rlibdir}/sgeostat/DESCRIPTION
%doc %{rlibdir}/sgeostat/html
%{rlibdir}/sgeostat/LICENSE
%{rlibdir}/sgeostat/NAMESPACE
%{rlibdir}/sgeostat/data
%{rlibdir}/sgeostat/INDEX
%{rlibdir}/sgeostat/R
%{rlibdir}/sgeostat/help
%{rlibdir}/sgeostat/Meta
%{rlibdir}/sgeostat/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.23-1
- initial package for Fedora