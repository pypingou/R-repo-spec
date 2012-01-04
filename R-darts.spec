%global packname  darts
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Statistical Tools to Analyze Your Darts Game

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Are you aiming at the right spot in darts? Maybe not! Use this package to
find your optimal aiming location. For a better explanation, go to
http://www-stat.stanford.edu/~ryantibs/darts/ or see the paper "A
Statistician Plays Darts".

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
%doc %{rlibdir}/darts/html
%doc %{rlibdir}/darts/DESCRIPTION
%{rlibdir}/darts/libs
%{rlibdir}/darts/Meta
%{rlibdir}/darts/NAMESPACE
%{rlibdir}/darts/R
%{rlibdir}/darts/help
%{rlibdir}/darts/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora