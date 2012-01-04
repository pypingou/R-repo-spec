%global packname  classInt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.17
Release:          1%{?dist}
Summary:          Choose univariate class intervals

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-17.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grDevices R-stats R-class R-e1071 

BuildRequires:    R-devel tex(latex) R-grDevices R-stats R-class R-e1071 

%description
A package for choosing univariate class intervals for mapping or other
graphics purposes

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.17-1
- initial package for Fedora