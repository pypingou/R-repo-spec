%global packname  Rcmdr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7.2
Release:          1%{?dist}
Summary:          R Commander

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-grDevices R-utils R-car 

BuildRequires:    R-devel tex(latex) R-tcltk R-grDevices R-utils R-car 

%description
 A platform-independent basic-statistics GUI (graphical user interface)
for R, based on the tcltk package.

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.2-1
- initial package for Fedora