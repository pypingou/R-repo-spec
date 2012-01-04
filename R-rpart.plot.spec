%global packname  rpart.plot
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Plot rpart models.  An enhanced version of plot.rpart.

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rpart 

BuildRequires:    R-devel tex(latex) R-rpart 

%description
Plot rpart models. Extends plot.rpart and text.rpart in the rpart package.

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
%doc %{rlibdir}/rpart.plot/doc
%doc %{rlibdir}/rpart.plot/DESCRIPTION
%doc %{rlibdir}/rpart.plot/html
%doc %{rlibdir}/rpart.plot/NEWS
%doc %{rlibdir}/rpart.plot/LICENCE
%{rlibdir}/rpart.plot/help
%{rlibdir}/rpart.plot/Meta
%{rlibdir}/rpart.plot/libs
%{rlibdir}/rpart.plot/data
%{rlibdir}/rpart.plot/NAMESPACE
%{rlibdir}/rpart.plot/R
%{rlibdir}/rpart.plot/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora