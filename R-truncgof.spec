%global packname  truncgof
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          GoF tests allowing for left truncated data

Group:            Applications/Engineering 
License:          GPL (version 2 or later)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Goodness-of-fit tests and some adjusted exploratory tools allowing for
left truncated data

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
%doc %{rlibdir}/truncgof/html
%doc %{rlibdir}/truncgof/DESCRIPTION
%{rlibdir}/truncgof/libs
%{rlibdir}/truncgof/R
%{rlibdir}/truncgof/help
%{rlibdir}/truncgof/INDEX
%{rlibdir}/truncgof/Meta
%{rlibdir}/truncgof/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.2-1
- initial package for Fedora