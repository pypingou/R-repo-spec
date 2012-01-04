%global packname  RFreak
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.7
Release:          1%{?dist}
Summary:          R/FrEAK interface

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rJava 
Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-rJava
BuildRequires:    R-methods 


%description
An R interface to a modified version of the Free Evolutionary Algorithm
Kit FrEAK. FrEAK is a toolkit written in Java to design and analyze
evolutionary algorithms. Both the R interface and an extended version of
FrEAK are contained in the RFreak package. For more information on FrEAK
see http://sourceforge.net/projects/freak427/.

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
%doc %{rlibdir}/RFreak/html
%doc %{rlibdir}/RFreak/DESCRIPTION
%doc %{rlibdir}/RFreak/doc
%{rlibdir}/RFreak/java
%{rlibdir}/RFreak/R
%{rlibdir}/RFreak/NAMESPACE
%{rlibdir}/RFreak/data
%{rlibdir}/RFreak/help
%{rlibdir}/RFreak/Meta
%{rlibdir}/RFreak/INDEX
RPM build errors:

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.7-1
- initial package for Fedora