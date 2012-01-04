%global packname  SASmixed
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Data sets from "SAS System for Mixed Models"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Data sets and sample lmer analyses corresponding to the examples in
Littel, Milliken, Stroup and Wolfinger (1996), "SAS System for Mixed
Models", SAS Institute.

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
%doc %{rlibdir}/SASmixed/doc
%doc %{rlibdir}/SASmixed/DESCRIPTION
%doc %{rlibdir}/SASmixed/html
%{rlibdir}/SASmixed/NAMESPACE
%{rlibdir}/SASmixed/Meta
%{rlibdir}/SASmixed/transcripts
%{rlibdir}/SASmixed/INDEX
%{rlibdir}/SASmixed/help
%{rlibdir}/SASmixed/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora