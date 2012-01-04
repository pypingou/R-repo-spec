%global packname  partitions
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9.10
Release:          1%{?dist}
Summary:          Additive partitions of integers

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.9-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-polynom 

BuildRequires:    R-devel tex(latex) R-polynom 

%description
Additive partitions of integers.  Enumerates the partitions, unequal
partitions, and restricted partitions of an integer; the three
corresponding partition functions are also given.  Set partitions are now

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.10-1
- initial package for Fedora