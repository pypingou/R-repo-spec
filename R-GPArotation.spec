%global packname  GPArotation
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2010.07.1
Release:          1%{?dist}
Summary:          GPA Factor Rotation

Group:            Applications/Engineering 
License:          GPL (>= 2) | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2010.07-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Gradient Projection Algorithm Rotation for Factor Analysis. See
?GPArotation.Intro for more details.

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
%doc %{rlibdir}/GPArotation/html
%doc %{rlibdir}/GPArotation/NEWS
%doc %{rlibdir}/GPArotation/DESCRIPTION
%doc %{rlibdir}/GPArotation/CITATION
%doc %{rlibdir}/GPArotation/doc
%{rlibdir}/GPArotation/NAMESPACE
%{rlibdir}/GPArotation/Meta
%{rlibdir}/GPArotation/help
%{rlibdir}/GPArotation/LICENSE
%{rlibdir}/GPArotation/INDEX
%{rlibdir}/GPArotation/data
%{rlibdir}/GPArotation/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2010.07.1-1
- initial package for Fedora