%global packname  latticist
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.43
Release:          1%{?dist}
Summary:          A graphical user interface for exploratory visualisation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-43.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-latticeExtra R-vcd 
Requires:         R-gWidgets 

BuildRequires:    R-devel tex(latex) R-lattice R-latticeExtra R-vcd
BuildRequires:    R-gWidgets 


%description
Latticist provides a graphical user interface for exploratory
visualisation. It is primarily an interface to the Lattice graphics
system, but also produces displays from the vcd package for categorical
data. Given a multivariate dataset (either a data frame or a table),
latticist attempts to produce useful displays based on the properties of
the data. The displays can be customised by editing the calls used to
generate them.

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
%doc %{rlibdir}/latticist/NEWS
%doc %{rlibdir}/latticist/html
%doc %{rlibdir}/latticist/CITATION
%doc %{rlibdir}/latticist/DESCRIPTION
%doc %{rlibdir}/latticist/doc
%{rlibdir}/latticist/etc
%{rlibdir}/latticist/Meta
%{rlibdir}/latticist/help
%{rlibdir}/latticist/INDEX
%{rlibdir}/latticist/R
%{rlibdir}/latticist/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.43-1
- initial package for Fedora