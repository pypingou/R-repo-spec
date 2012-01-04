%global packname  maxstat
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.14
Release:          1%{?dist}
Summary:          Maximally Selected Rank Statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-exactRankTests R-mvtnorm R-survival 

BuildRequires:    R-devel tex(latex) R-exactRankTests R-mvtnorm R-survival 

%description
Maximally selected rank statistics with several p-value approximations.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.14-1
- initial package for Fedora